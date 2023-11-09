from mininet.net import Mininet, OVSKernelSwitch

from mininet.node import Controller, RemoteController

from mininet.cli import CLI

from mininet.log import setLogLevel, info



def topology():

    "Create a network with 2 controllers, 2 switches and 4 hosts."

    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)



    info('*** Adding controllers\n')

    c1 = net.addController('c1', controller=RemoteController, ip="127.0.0.1", port=6633)

    c2 = net.addController('c2', controller=RemoteController, ip="127.0.0.1", port=6655)



    info('*** Adding switches\n')  

    s1 = net.addSwitch('s1', cls=OVSKernelSwitch) # "cls" This specifies the class of the switch. In this case, OVSKernelSwitch is used, which is a class for Open vSwitch switches that use the Linux kernel-based switch implementation2.

    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)

  



    info('*** Adding hosts\n')

    h1 = net.addHost('h1')

    h2 = net.addHost('h2')

    h3 = net.addHost('h3')

    h4 = net.addHost('h4')



    info('*** Creating links\n')

    # Add link from controller1 to switch 1.

    #net.addLink(c1, s1)

    info('*** Added link between c1 and s1\n')

    # Add link from controller2 to switch 2.

    #net.addLink(c2, s2)

    info('*** Added link between c2 and s2\n')

    #Add link from switch 1 to container 1.

    net.addLink(s1, h1)

    #Add link from switch 1 to container 2.

    net.addLink(s1, h2)

    #Add link from switch 2 to container 3.

    net.addLink(s2, h3)

    #Add link from switch 2 to container 4.

    net.addLink(s2, h4)

    #Add link from switch 2 to container 1.

    net.addLink(s2, h1)





    # net.addLink(h1, s1)

    # net.addLink(h2, s1)

    # net.addLink(h3, s2)

    # net.addLink(h4, s2)

    # net.addLink(s1, s2)



    info('*** Starting network\n')

    net.build()

    c1.start()

    c2.start()

    s1.start([c1])

    s2.start([c2])



    info('*** Running CLI\n')

    CLI(net)



    info('*** Stopping network')

    net.stop()



if __name__ == '__main__':

    setLogLevel('info')

    topology()

