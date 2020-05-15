import os

class Main:
    templates = []
    def __init__(self, main):
        self.main = main
        os.chdir(os.path.join(main.main_path, "assets", "te"))
        self.import_templates()

        print(self.templates)

    def import_templates(self):
        for fname in os.listdir():
            if fname[-3:] == ".py":
                t = __import__(fname[:-3])
                tile_ids_start = t.tile_ids_start
                tile_ids = t.tile_ids
                del t

                t_len = len(self.templates) - 1
                len_to_add = tile_ids_start - t_len + 1
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
                    
    