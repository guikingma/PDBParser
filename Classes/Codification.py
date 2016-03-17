class Codification:
	""" Codification. """
	codification = {}

	def __init__(self):
		#self.codification = {'ALA':1.0, 'ARG':2.0, 'ASN':3.0, 'ASP':4.0, 'CYS':5.0, 'GLU':6.0, 'GLN':7.0, 'GLY':8.0, 'HIS':9.0, 'ILE':10.0, 'LEU':11.0, 'LYS':12.0, 'MET':13.0, 'PHE':14.0, 'PRO':15.0, 'SER':16.0, 'THR':17.0, 'TRP':18.0, 'TYR':19.0, 'VAL':20.0, 'N':21.0, 'H':22.0, 'S':23.0, 'MSE':24.0, 'CME':25.0, 'ACE':26.0, 'PCA':27.0, 'CAS':28.0, 'CSO':29.0, 'FME':30.0, 'MHS':31.0, 'AGM':32.0, 'MGN':33.0, 'GL3':34.0, 'SMC':35.0, 'TRQ':36.0, 'GPL':37.0, 'CSS':38.0, 'BCS':39.0, 'TPO':40.0, 'OCS':41.0, 'PTR':42.0, 'ABA':43.0, 'DG':44.0, 'DA':45.0, 'DC':46.0, 'DT':47.0, 'EDA':48.0, 'KCX':49.0, 'CGU':50.0, 'PED':51.0, '3DR':52.0, 'NH2':53.0, 'BOC':54.0, 'APE':55.0, 'CSD':56.0, '8OG':57.0, 'G':58.0, 'C':59.0, 'A':60.0, 'U':61.0, 'FHU':62.0, 'MLZ':63.0, 'MLY':64.0, 'PHD':65.0, 'SEP':66.0}
		self.codification = {'ALA':12.0, 'ARG':38.0, 'ASN':32.0, 'ASP':33.0, 'CYS':17.0, 'GLU':34.0, 'GLN':16.0, 'GLY':29.0, 'HIS':39.0, 'ILE':8.0, 'LEU':4.0, 'LYS':37.0, 'MET':9.0, 'PHE':3.0, 'PRO':36.0, 'SER':23.0, 'THR':26.0, 'TRP':1.0, 'TYR':2.0, 'VAL':11.0, 'N':11, 'H':10, 'S':01, 'MSE':47.0, 'CME':55.0, 'ACE':40.0, 'PCA':35.0, 'CAS':71.0, 'CSO':19.0, 'FME':10.0, 'MHS':72.0, 'AGM':73.0, 'MGN':74.0, 'GL3':75.0, 'SMC':76.0, 'TRQ':79.0, 'GPL':68.0, 'CSS':67.0, 'BCS':70.0, 'TPO':69.0, 'OCS':51.0, 'PTR':48.0, 'ABA':49.0, 'DG':30.0, 'DA':13.0, 'DC':20.0, 'DT':27.0, 'EDA':53.0, 'KCX':62.0, 'CGU':80.0, 'PED':58.0, '3DR':61.0, 'NH2':42.0, 'BOC':59.0, 'APE':60.0, 'CSD':56.0,  'G':82.0, 'C':81.0, 'U':83.0, 'FHU':89.0, 'MLZ':63.0, 'MLY':64.0, 'PHD':66.0, 'SEP':65.0, '8OG':57.0, 'A':52.0}

	def getValue(self, key):
		""" Returns the corresponding value of the given key """
		
		return self.codification[key]