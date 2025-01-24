require 'rugged'
require 'linguist'

repo = Rugged::Repository.new('/Users/askborgen/Desktop/code/')
project = Linguist::Repository.new(repo, repo.head.target_id)
project.language       #=> "Ruby"
puts project.languages();      #=> { "Ruby" => 119387 }