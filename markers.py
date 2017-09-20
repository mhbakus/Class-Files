class Marker:
    def __init__(self, color="Red"):
        self.color = color

    def __repr__(self):
        return "This is a {} marker".format(self.color)

class MarkerBox:
    def __init__(self, markers = []):
        self.markers = markers
    
    def __repr__(self):
        marker_str = ""
        for marker in self.markers:
            marker_str += str(marker) + "\n"
        return marker_str

    def add_marker(self, marker):
        self.markers.append(marker)

    def remove_marker(self, color):
        for marker in self.markers:
            if marker.color == color:
                return marker
        return none

if __name__ == "__main__":
    mest_markers = MarkerBox()
    new_marker = Marker(color="blue")
    print(new_marker)
    mest_markers.add_marker(Marker(color="blue"))
    mest_markers.add_marker(Marker(color="red"))
    mest_markers.add_marker(Marker(color="green"))
    #mest_markers.remove_marker("black")
