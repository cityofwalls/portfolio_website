module ApplicationHelper
    
    def active_class(link_path)
        current_page?(link_path) ? "nav-item active" : "nav-item"
    end
    
    def dropdown_active_class()
        current_page?(python_path) || current_page?(java_path) || current_page?(go_path) || current_page?(swift_path) || current_page?(ml_path) ? "nav-item dropdown active" : "nav-item dropdown"
    end
    
end
