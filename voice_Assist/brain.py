import torch.nn as nn 

class NeuralNetwork(nn.Module):
    def __init__(self,inputs,hidden,outputs):
        super(NeuralNetwork,self).__init__()
        self.LayerOne    = nn.Linear(inputs,hidden)
        self.LayerTwo    = nn.Linear(hidden,hidden)
        self.LayerThree  = nn.Linear(hidden,hidden)
        self.LayerFour   = nn.Linear(hidden,hidden)
        self.LayerFive   = nn.Linear(hidden,outputs)
        self.relu        = nn.ReLU()
        
    def forward(self,x):
        out = self.LayerOne(x)
        out = self.relu(out)
        out = self.LayerTwo(out)
        out = self.relu(out)
        out = self.LayerThree(out) 
        out = self.relu(out)
        out = self.LayerFour(out) 
        out = self.relu(out)
        out = self.LayerFive(out) 
        return out