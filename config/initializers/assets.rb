# Be sure to restart your server when you modify this file.

# Version of your assets, change this if you want to expire all your assets.
Rails.application.config.assets.version = '1.0'

# Add additional assets to the asset load path.
# Rails.application.config.assets.paths << Emoji.images_path
# Add Yarn node_modules folder to the asset load path.
Rails.application.config.assets.paths << Rails.root.join('node_modules')

# Add custom asset folders to asset pipeline
# From: https://stackoverflow.com/questions/23192298/add-a-new-folder-to-asset-path-in-rails-4
Rails.application.config.assets.enabled = true
Rails.application.config.assets.paths << Rails.root.join("app", "assets", "plugins", "frogger", "py")

# Precompile additional assets.
# application.js, application.css, and all non-JS/CSS in the app/assets
# folder are already added.
# Rails.application.config.assets.precompile += %w( admin.js admin.css )

# Configure CSS assets here
Rails.application.config.assets.precompile += %w( application.scss )
Rails.application.config.assets.precompile += %w( home.css )

Rails.application.config.assets.precompile += %w( resume_style.css )

Rails.application.config.assets.precompile += %w( python_style.css )
Rails.application.config.assets.precompile += %w( java_style.css )
Rails.application.config.assets.precompile += %w( go_style.css )
Rails.application.config.assets.precompile += %w( swift_style.css )
Rails.application.config.assets.precompile += %w( ml_style.css )
Rails.application.config.assets.precompile += %w( flappy_style.css )
Rails.application.config.assets.precompile += %w( pong_style.css )

Rails.application.config.assets.precompile += %w( music_style.css )

Rails.application.config.assets.precompile += %w( connect_style.css )

# Configure JS assets here
# -- skulpt and codeskulptor js files for python.html.erb
Rails.application.config.assets.precompile += %w( skulpt.min.js )
Rails.application.config.assets.precompile += %w( codeskulptor-compressed.js )

Rails.application.config.assets.precompile += %w( nn.js )
Rails.application.config.assets.precompile += %w( matrix.js )
Rails.application.config.assets.precompile += %w( sketch_flappy.js )
Rails.application.config.assets.precompile += %w( bird.js )
Rails.application.config.assets.precompile += %w( pipe.js )
Rails.application.config.assets.precompile += %w( ga_flappy.js )

# -- home.js for home.html.erb
Rails.application.config.assets.precompile += %w( home.js )
