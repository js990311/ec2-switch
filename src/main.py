from src.aws.ec2_handler_factory import ec2_handler_factory
from src.gui.app_view import AppView
from src.utils.config_manager import load_config_file, get_path

if __name__ == "__main__":
    config = load_config_file()
    ec2Handler = ec2_handler_factory(config)
    app = AppView(ec2Handler)
    app.mainloop()
