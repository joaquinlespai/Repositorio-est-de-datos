importar  al azar
 sistema de importación
de  PyQt6 . QtWidgets  importa  QApplication , QWidget , QPushButton
de  PyQt6 . QtGui  importar  QColor

clase  Ventana ( QWidget ):
    def  __init__ ( auto ):
        súper (). __inicio__ ()

        uno mismo setGeometry ( 200 , 200 , 300 , 200 )
        uno mismo setWindowTitle ( "Botón colorido" )

        uno mismo boton  =  QPushButton ( "Presiona" , self )
        uno mismo botón _ setGeometry ( 100 , 80 , 100 , 50 )
        uno mismo botón _ hizo clic conectar ( self . cambiar_color )

    def  cambiar_color ( auto ):
        color  =  QColor ( aleatorio . randint ( 0 , 255 ), aleatorio . randint ( 0 , 255 ), aleatorio . randint ( 0 , 255 ))
        uno mismo botón _ setStyleSheet ( "color de fondo: {}" . formato ( color . nombre ()))

si  __nombre__  ==  "__principal__" :
    app  =  QApplication ( sys . argv )
    ventana  =  ventana ()
    ventana . mostrar ()
    sistema _ salir ( aplicación . exec ())