class Dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.children = {}
        self.files = {}
        self.size = 0


class File:
    def __init__(self, parent, size, name):
        self.parent = parent
        self.name = name
        self.size = size


def print_fs(node):
    print(node.name)
    files = ",".join([fname for fname in node.files])
    print(f"has files: {files}")
    for child, childNode in node.children.items():
        print_fs(childNode)


sizes = []
size_to_delete = 70000000


def assign_sizes(node):
    direct_file_sizes = 0
    for f, f_node in node.files.items():
        direct_file_sizes += f_node.size
    children_sizes = []
    for c, c_node in node.children.items():
        children_sizes.append(assign_sizes(c_node))
    node.size = direct_file_sizes + sum(children_sizes)
    sizes.append(node.size)
    return node.size


def check_for_deletion(node, needed_size):
    global size_to_delete

    if node.size >= needed_size and node.size < size_to_delete:
        size_to_delete = node.size
    for c, c_node in node.children.items():
        check_for_deletion(c_node, needed_size)


root = Dir(None, '/')
current_dir = root

output = open('input.txt')

for line in output:
    l = line.strip()
    parts = l.split()
    if (parts[0] == '$'):
        if (parts[1] == 'cd'):
            if (parts[2] == '/'):
                current_dir = root
            elif (parts[2] == '..'):
                if current_dir.parent == None:
                    raise Exception('No directory to go back to!')
                current_dir = current_dir.parent
            else:
                next_dir = parts[2]
                if (next_dir not in current_dir.children):
                    dir_node = Dir(current_dir, next_dir)
                    current_dir.children[next_dir] = dir_node
                    current_dir = dir_node
                current_dir = current_dir.children[next_dir]

        elif (parts[1] == 'ls'):
            continue
    else:
        # files and directories list
        content_parts = l.split()
        if content_parts[0] == 'dir':
            dir = content_parts[1]
            if dir not in current_dir.children:
                dir_node = Dir(current_dir, dir)
                current_dir.children[dir] = dir_node
        else:
            # it's a file
            size = int(content_parts[0])
            fname = content_parts[1]
            if fname not in current_dir.files:
                file = File(current_dir, size, fname)
                current_dir.files[fname] = file

assign_sizes(root)

total_size = root.size
unused_space = 70000000 - total_size
required_space = 30000000 - unused_space

check_for_deletion(root, required_space)
print(size_to_delete)
