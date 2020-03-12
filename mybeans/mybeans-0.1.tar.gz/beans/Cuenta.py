class Cuenta:
    def __init__(self, titular, cantidad):
        self.__titular = titular
        if (cantidad<0):
            self.__cantidad = 0
        else:
            self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular


    def get_cantidad(self):
        return self.__cantidad


    def set_titular(self, value):
        self.__titular = value


    def set_cantidad(self, value):
        self.__cantidad = value


    def del_titular(self):
        del self.__titular


    def del_cantidad(self):
        del self.__cantidad

    #titular = property(get_titular, set_titular, del_titular, "titular's docstring")
    #cantidad = property(get_cantidad, set_cantidad, del_cantidad, "cantidad's docstring")
    
    '''
    **
     * Ingresa dinero en la cuenta, 
     * solo si es positivo la cantidad
     *
     * @param cantidad
     */
     '''
    def ingresar(self, cantidad): 
        if (cantidad > 0):
            self.set_cantidad(self.get_cantidad()+cantidad)
    '''
    /**
     * Retira una cantidad en la cuenta, si se quedara en negativo se quedaria
     * en cero
     *
     * @param cantidad
     */
     '''
    def retirar(self, cantidad):
        if (self.__cantidad - cantidad < 0):
            self.set_cantidad(0)
        else:
            self.__cantidad -= cantidad;
    
    def __str__(self):
        return "El titular " + self.get_titular() + " tiene " + str(self.get_cantidad()) + " euros en la cuenta"

    