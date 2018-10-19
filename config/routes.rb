Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  
  # Homepage
  root to: "pages#home"
  
  # Routes to other static pages (this removes the need for pages/resume and is now /resume as a route)
  get "/resume" => "pages#resume"
  get "/code" => "pages#code"
  get "music" => "pages#music"
  get "/connect" => "pages#connect"
end
