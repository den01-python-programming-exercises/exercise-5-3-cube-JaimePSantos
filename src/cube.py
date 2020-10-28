class Cube:
  def __init__(self,edge_length):
    self.edge_length = edge_length
  
  def volume(self):
    return self.edge_length**3
  
  def __str__(self):
    return "The length of the edge is %s and the volume %s"%(self.edge_length,self.volume())