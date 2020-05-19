import os, importlib, sys
import_module = importlib.import_module
path_insert = sys.path.insert
path_join = os.path.join

class Main:
    templates = []
    def __init__(self, main):
        self.main = main
        templates_path = path_join(main.mainpath, "assets", "templates")
        os.chdir(templates_path)
        path_insert(0, templates_path)  

        self.import_templates()

        print(self.templates)

    def import_templates(self):
        for fname in os.listdir():
            if fname[-3:] == ".py":
                t = import_module(fname[:-3])
                tile_ids_start = t.tile_ids_start
                tile_ids = t.tile_ids
                del t

                t_len = len(self.templates)
                len_to_add = tile_ids_start - t_len
                if len_to_add > 0:
                    self.templates += [None] * len_to_add
                
                for i in range(tile_ids_start, tile_ids_start+len(tile_ids)):
                    if i < t_len:
                        if self.templates[i] is None:
                            self.templates[i] = tile_ids.pop(0)
                        else:
                            print(f"Template Tile id {i} Overlap!!!")
                            quit()
                    else:
                        self.templates.append(tile_ids.pop(0))
                    