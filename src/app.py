from views.menu import Menu
from utils import logs

def main():
    instance = Menu()
    logs.start_app()
    instance.start_view()

if __name__ == '__main__':
    main()