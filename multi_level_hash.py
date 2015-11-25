#auto_vivication

# create mechanism similar to perl $hash{$key1}{$key2} = $value

class hash(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value



dict = hash()
dict[key1][key2] = value


