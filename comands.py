from config import Manager
import os

working_dir = os.getcwd()
file_manager = Manager(working_dir)

commands = {
    'help': 'help',
    'exit': 'exit',
    'create_dir': lambda arg: file_manager.create_dir(arg),
    'to_root_dir': 'to_root_dir',
    'delete_dir': lambda arg: file_manager.delete_dir(arg),
    'change_dir': lambda arg: file_manager.change_dir(arg),
    'create_file': lambda arg: file_manager.create_file(arg),
    'read_file': lambda arg: file_manager.read_file(arg),
    'write_file': lambda args: file_manager.write_file(*args.split()),
    'delete_file': lambda args: file_manager.delete_file(arg),
    'copy_file': lambda args: file_manager.copy_file(*args.split()),
    'move_file': lambda args: file_manager.move_file(*args.split()),
    'rename_file': lambda args: file_manager.rename_file(*args.split())
}