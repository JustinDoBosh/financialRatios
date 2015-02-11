import locale 
locale.setlocale( locale.LC_ALL, '' )

class finance:
	def __init__(self):
		pass

	def WeightedAvgCostCap(self):
		print "\n******WACC Calculator******\n"
		#Collect data
		Re = raw_input("Cost of equity")
		Rd = raw_input("Cost of debt")
		E = raw_input("Market value of the firm's equity")
		D = raw_input("Market value of the firm's debt")
		Tc = raw_input("Corporate tax rate")
		#Clean collected data
		Re = float(Re)
		Rd = float(Rd)
		E = float(E)
		D = float(D)
		Tc = float(Tc)
		#Convert into decimals
		Re = Re / 100
		Rd = Rd / 100
		Tc = Tc / 100
		#Perform calculations
		V = E + D
		equityPercentage = E / V
		debtPercentage = D / V
		corpTaxRate = 1 - Tc
		wacc = ((equityPercentage * Re) + (debtPercentage * Rd * corpTaxRate))
		#Clean and print wacc
		wacc = str(wacc * 100)
		print "The weighted average cost of capital is " + wacc + "%"

	def EnterpriseValue(self):
		print "\n******Enterprise Value Calculator******\n"
		#Get data
		StkPrice = raw_input("Current stock price: ")
		SO = raw_input("Shares outstanding: ")
		TD = raw_input("Total debt: ")
		TC = raw_input("Total cash: ")
		#Clean data
		StkPrice = float(StkPrice)
		SO = int(SO)
		TD = float(TD)
		TC = float(TC)
		#Perform calculations
		MktCap = StkPrice * SO 
		EV = MktCap + TD - TC
		#Format and print EV
		EV = locale.currency(EV, grouping=True)
		print "The enterprise value of the firm is " +  EV

	def ReturnOnInv(self):
		#Get data
		gain = raw_input("Gain from investment: ")
		cost = raw_input("Cost of investment: ")
		#Clean data
		gain = float(gain)
		cost = float(cost)
		#Perform calculations
		ROI = (gain - cost) / cost
		#Format and print ROI
		ROI = str(ROI * 100)
		print "The return on invesment is " + ROI + "%"

	def LiquidityRatios(self):
		#Get data
		CA = raw_input("Current assets: ")
		CL = raw_input("Current liabilities: ")
		Inventory = raw_input("Inventory: ")
		#Clean data
		CA = float(CA)
		CL = float(CL)
		Inventory = float(Inventory)

		#Current ratio calculation 
		currentRatio = CA / CL 
		#Format and print current ratio
		currentRatio = round(currentRatio,2)
		currentRatio = str(currentRatio)
		print "\nThe current ratio is " + currentRatio + "\n"

		#Quick ratio calculation
		quickRatio = (CA - Inventory) / CL
		#Format and print quick ratio
		quickRatio = round(quickRatio,2)
		quickRatio = str(quickRatio)
		print "\nThe quick ratio is " + quickRatio + "\n"

		#Working capital calculation 
		workingCap = CA - CL 
		workingCap = round(workingCap,2)
		workingCap = locale.currency(workingCap, grouping=True)
		print "\nThe firm's working capital is " + workingCap + "\n"

	def FinancialLeverageRatios(self):
		#Get data
		TD = raw_input("Total debt: ")
		TA = raw_input("Total assets: ")
		TE = raw_input("Total equity: ")
		EBIT = raw_input("EBIT : ")
		IntExp = raw_input("Interest expense: ")
		#Clean data
		TD = float(TD)
		TA = float(TA)
		TE = float(TE)
		EBIT = float(EBIT)
		IntExp = float(IntExp)
		#Calculate debt ratio
		DebtRatio = TD / TA
		#Format and print debt ratio 
		DebtRatio = round(DebtRatio,2)
		DebtRatio = str(DebtRatio)
		print "\nThe debt ratio is " + DebtRatio + "\n"

		#Calculate debt to equity ratio
		D2ERatio = TD / TE
		#Format and print debt ratio 
		D2ERatio = round(D2ERatio,2)
		D2ERatio = str(D2ERatio)
		print "\nThe debt to equity ratio is " + D2ERatio + "\n"

		#Calculate interest coverage ratio
		IntCoverageRatio = EBIT / IntExp
		#Format and print interest coverage ratio 
		IntCoverageRatio = round(IntCoverageRatio,2)
		IntCoverageRatio = str(IntCoverageRatio)
		print "\nThe interest coverage ratio is " + IntCoverageRatio + "\n"

	def ProfitabilityRatios(self):
		#Get data
		sales = raw_input("Sales: ")
		COGS = raw_input("Cost of goods sold: ")
		NI = raw_input("Net income: ")
		TA = raw_input("Total assets: ")
		SE = raw_input("Shareholder Equity: ")
		#Clean data
		sales = float(sales)
		COGS = float(COGS)
		NI = float(NI)
		TA = float(TA)
		SE = float(SE)
		#Calculate gross profit margin 
		GPM = (sales - COGS) / sales
		GPM = round(GPM,2)
		GPM = str(GPM)
		print "\n The firm's gross profit margin is " + GPM + "\n"
		#Calculate ROA
		ROA = NI / TA
		ROA = round(ROA,2)
		ROA = str(ROA)
		print "\n The firm's return on assets is " + ROA + "\n"
		#Calculate ROE
		ROE = NI / SE
		ROE = round(ROE,2)
		ROE = str(ROE)
		print "\n The firm's return on equity is " + ROE + "\n"

	def DividendRatios(self):
		#Get data
		DPS = raw_input("Dividends per share: ")
		SP = raw_input("Share price: ")
		EPS = raw_input("Earnings per share: ")
		#Clean data
		DPS = float(DPS)
		SP = float(SP)
		EPS = float(EPS)
		#Calculate dividend yield
		DY = DPS / SP
		DY = DY * 100
		DY = round(DY,2)
		DY = str(DY)
		print "\n The firm's dividend yield is " + DY + "%\n"
		#Calculate dividend payout ratio
		DPR = DPS / EPS
		DPR = DPR * 100
		DPR = round(DPR,2)
		DPR = str(DPR)
		print "\n The firm's dividend payout ratio is " + DPR + "%\n"


companyX = finance()
#companyX.WeightedAvgCostCap()
#companyX.EnterpriseValue()
#companyX.ReturnOnInv()
#companyX.LiquidityRatios()
#companyX.FinancialLeverageRatios()
#companyX.ProfitabilityRatios()
#companyX.DividendRatios()