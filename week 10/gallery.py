class ArtPiece:
    def __init__(self, title, artist, price):
        self.title = title
        self.artist = artist
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        # only allow price increases
        if new_price > self._price:
            self._price = new_price

    def __str__(self):
        return f"{self.title} by {self.artist} (£{self.price})"


class Exhibition:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.art_pieces = []

    def add_piece(self, piece):
        if piece not in self.art_pieces:
            self.art_pieces.append(piece)

    def remove_piece(self, title, artist):
        for p in self.art_pieces:
            if p.title == title and p.artist == artist:
                self.art_pieces.remove(p)
                return  

    def total_value(self):
        total = 0
        for p in self.art_pieces:
            total += p.price
        return total

    def __str__(self):
        text = f"Exhibition: {self.name}\n"
        text += f"Dates: {self.start_date} -> {self.end_date}\n"
        text += "Art pieces:\n"
        if not self.art_pieces:
            text += "  (none)\n"
        else:
            for p in self.art_pieces:
                text += f"  {p.title} by {p.artist} (£{p.price})\n"
        text += f"Total value: £{self.total_value()}\n"
        return text


class Gallery:
    def __init__(self, name):
        self.name = name
        self.exhibitions = []

    def host_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)

    def __str__(self):
        text = f"Gallery: {self.name}\n"
        for ex in self.exhibitions:
            text += f"{ex.name} ({ex.start_date} --> {ex.end_date})\n"
        return text


def test_gallery():
    # Create art pieces
    p1 = ArtPiece("Sunset Over Water", "A. Khan", 1200)
    p2 = ArtPiece("City Noise", "M. Rivera", 850)
    p3 = ArtPiece("Quiet Forest", "A. Khan", 1500)
    p4 = ArtPiece("Blue Geometry", "S. Patel", 500)
    p5 = ArtPiece("Portrait in Grey", "J. Smith", 950)

    
    ex1 = Exhibition("Urban & Light", "10-02-2026", "10-03-2026")
    ex2 = Exhibition("Shapes of Calm", "15-03-2026", "05-04-2026")

    ex1.add_piece(p1)
    ex1.add_piece(p2)
    ex1.add_piece(p4)

    ex2.add_piece(p3)
    ex2.add_piece(p4)
    ex2.add_piece(p5)

    ex1.remove_piece("Blue Geometry", "S. Patel")

    # Update prices
    p1.price = 1300
    p3.price = 1400   

    # exhibitions
    gallery = Gallery("Portsmouth Modern Art")
    gallery.host_exhibition(ex1)
    gallery.host_exhibition(ex2)

    print(gallery)
    print(ex1)
    print(ex2)


test_gallery()