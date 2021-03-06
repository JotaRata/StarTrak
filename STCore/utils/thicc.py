from matplotlib import pylab as plt

# Actualizacion: Cambie reference1, reference2 y variable a una sola lista
def thicc(reference1,reference2,variable,time):
    f, pl = plt.subplots()
    pl.plot(time,reference1,"o")
    pl.plot(time,reference2,'o')
    pl.plot(time,variable,'o')
    plt.xlabel("Tiempo")
    plt.ylabel("Magnitud")
    plt.ylim(np.max([np.max(variable),np.max(reference1),np.max(reference2)])+3,\
             np.min([np.min(variable),np.min(reference1),np.min(reference2)])-3)
    return pl
