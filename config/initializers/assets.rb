# Be sure to restart your server when you modify this file.

# Version of your assets, change this if you want to expire all your assets.
Rails.application.config.assets.version = '1.0'

# Add additional assets to the asset load path.
# Rails.application.config.assets.paths << Emoji.images_path
# Add Yarn node_modules folder to the asset load path.
Rails.application.config.assets.paths << Rails.root.join('node_modules')

# Precompile additional assets.
# application.js, application.css, and all non-JS/CSS in the app/assets
# folder are already added.
# Rails.application.config.assets.precompile += %w( admin.js admin.css )

# Configure CSS assets here
Rails.application.config.assets.precompile += %w( connect_style.css )
Rails.application.config.assets.precompile += %w( python_style.css )

# Configure JS assets here
# Rails.application.config.assets.precompile += %w( skulpt.min.js )
# Rails.application.config.assets.precompile += %w( numeric-1.2.6.min.js )
# Rails.application.config.assets.precompile += %w( jquery.flot.orderbars.min.js )
# Rails.application.config.assets.precompile += %w( jquery.flot.min.js )
Rails.application.config.assets.precompile += %w( codeskulptor-compressed.js )
# Rails.application.config.assets.precompile += %w( codemirror-compressed.js )

Rails.application.config.assets.precompile += %w( pythonrun.js )