from mininet.topo import Topo

class CustomTopo(Topo):
    def __init__(self):
        super(CustomTopo, self).__init__()

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add links between hosts and switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s3)
        self.addLink(h5, s3)

        # Add link between switches
        self.addLink(s1, s2)
        self.addLink(s2, s3)

topos = {'customtopo': (lambda: CustomTopo())}