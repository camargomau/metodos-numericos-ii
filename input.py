from sympy import sympify

class Input:
	def int(prompt):
		while True:
			try:
				answer = int(input(prompt))

				if answer < 1:
					raise IndexError

				break
			except IndexError:
				prompt = "-> Introduzca un número entero mayor o igual que 1: "
			except:
				prompt = "-> Introduzca un número entero: "

		return answer

	def real(prompt, size=1, separator=","):
		if size == 1:
			while True:
				try:
					answer = sympify(input(prompt))
					if not answer.is_real:
						raise ValueError
					break
				except:
					prompt = "-> Introduzca un número real: "
		else:
			while True:
				answer = input(prompt).strip().split(separator)
				if len(answer) != size:
					prompt = f"-> Introduzca exactamente {size} reales: "
					continue

				try:
					answer = [sympify(i) for i in answer]
					if not all(i.is_real for i in answer):
						raise ValueError
					break
				except ValueError:
					prompt = "-> Solo inserta números reales: "

		return answer
