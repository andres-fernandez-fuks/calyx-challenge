from project.processing.processor import Processor
from project import create_app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        Processor.start_process(app)