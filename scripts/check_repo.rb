# frozen_string_literal: true

ROOT = File.expand_path("..", __dir__)

REQUIRED_FILES = %w[
  .gitignore
  README.md
  DESIGN.md
].freeze

EXPECTED_IDS = {
  "Canon" => (1..15).map { |number| format("C%02d", number) },
  "Pattern" => (1..15).map { |number| format("P%02d", number) },
  "Motif" => ("A".."H").map { |letter| "M-#{letter}" },
  "Smell" => (1..15).map { |number| format("S%02d", number) }
}.freeze

LOCAL_ONLY_FILES = %w[
  AI_Playbook_DesignSystem_v1.1.html
  知識庫Playbook-母文件.md
  DECK_MAP.md
].freeze

errors = []

def read_repo_file(path)
  File.read(File.join(ROOT, path), encoding: "UTF-8")
end

def local_markdown_links(text)
  text.scan(/\[[^\]]+\]\(([^)]+)\)/).flatten.map do |target|
    next if target.start_with?("http://", "https://", "mailto:", "#")

    path = target.split("#", 2).first
    next unless path.end_with?(".md", ".rb")

    path
  end.compact
end

REQUIRED_FILES.each do |path|
  errors << "missing required file: #{path}" unless File.file?(File.join(ROOT, path))
end

unless errors.empty?
  warn errors.join("\n")
  exit 1
end

design = read_repo_file("DESIGN.md")
readme = read_repo_file("README.md")
gitignore = read_repo_file(".gitignore").lines.map(&:strip)

version = design[/^# Eric Presentation Design System v(\d+\.\d+)$/, 1]
errors << "DESIGN.md has no semantic version in its title" unless version
if version && !readme.include?("Eric Presentation Design System v#{version}")
  errors << "README version does not match DESIGN.md v#{version}"
end

actual_ids = {
  "Canon" => design.scan(/^## (C\d{2})\b/).flatten,
  "Pattern" => design.scan(/^## (P\d{2})\b/).flatten,
  "Motif" => design.scan(/^## (M-[A-H])\b/).flatten,
  "Smell" => design.scan(/^## (S\d{2})\b/).flatten
}

EXPECTED_IDS.each do |group, expected|
  actual = actual_ids.fetch(group)
  errors << "#{group} IDs are #{actual.inspect}; expected #{expected.inspect}" unless actual == expected
end

LOCAL_ONLY_FILES.each do |path|
  errors << "local-only file is not ignored: #{path}" unless gitignore.include?("/#{path}")
end

local_markdown_links(readme).each do |path|
  errors << "README links to missing file: #{path}" unless File.file?(File.join(ROOT, path))
end

if errors.empty?
  puts "PASS: README and DESIGN.md versions match at v#{version}."
  EXPECTED_IDS.each do |group, ids|
    puts "PASS: #{group} IDs are complete (#{ids.first}-#{ids.last})."
  end
  puts "PASS: project-specific examples are ignored."
  puts "PASS: README local links resolve."
else
  warn "REVISE: #{errors.length} problem(s) found:"
  errors.each { |error| warn "- #{error}" }
  exit 1
end
