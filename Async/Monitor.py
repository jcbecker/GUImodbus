
#essa classe so deve ser instanciada para testes
#na realidade e uma classe abstrata que vai ter filhos
#para serem utilizados pela classe MyThread.
class Monitor:

	#name e apenas um nome para ajudar nos testes
	#na classe thread, user e uma classe que vai
	#ser utilizada no metodo myTurn.
	def __init__( self, name, user ):
		self.name = name
		self.user = user

	def myTurn(self):
		print "My turn: " + self.name

		#colocar aqui o codigo que vai utilizar
		#a classe user
