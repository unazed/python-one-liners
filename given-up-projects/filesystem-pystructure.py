(globals().__setitem__("create_padded_buffer", lambda string, space, char="\x00": False if space < len(string) else string + char*(space-len(string))),globals().__setitem__("partial", __import__("functools").partial),globals().__setitem__("types", __import__("types")),globals().__setitem__("Superblock", __import__("superblock")),globals().__setitem__("_set_self",lambda globals_, self, name:setattr(self, name, globals_[name])),globals().__setitem__("PyStructure", type("PyStructure", (object,), {"__init__":lambda self, magic_header, version_number, vendor_name, superblock: (globals().__setitem__("set_self", partial(_set_self, locals())),setattr(self, "__doc__", """magic_header   => `bytearray` of FOUR bytes which represents the unique identifier of the FILE SYSTEM\nversion_number => `bytearray` of TWO bytes which represents the VERSION of the FILE SYSTEM\nvendor_name    => `str` of THIRTY-TWO bytes (with slack space) that represents the VENDOR of the FILE SYSTEM\nsuperblock     => `Superblock` <class> which contains the META DATA for the FILE SYSTEM's clusters etc."""),set_self(self, "magic_header"),set_self(self, "vendor_name"),set_self(self, "version_number"),set_self(self, "superblock"),None)[-1],"get_raw_buffer":lambda self:"%s%s%s%s" % (self.magic_header.decode()[:4],self.vendor_name[:32],self.version_number.decode()[:2],self.superblock.get_raw_buffer())})))