import wx
class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Construction Wizard', size=(400, 320)) # Overides the default window value.
        panel = wx.Panel(self) # Make self an instance of pannel

        #First question    
        wx.StaticText(panel, id=-1, label = "What's length of your house?", pos =(5, 20), style = 3, name = "test")
        
        #Second question
        wx.StaticText(panel, id=-1, label = "What's width of your house?", pos =(5, 80), style = 3, name = "test")

        # Box's
        self.first_box = wx.text_ctrl = wx.TextCtrl(panel, pos=(20, 40)) # Init
        self.second_box = wx.text_ctrl = wx.TextCtrl(panel, pos=(20, 100)) # Init
        self.report = wx.text_ctrl = wx.TextCtrl(panel, pos=(170, 20), size=(200,250)) # Init
        self.my_btn = wx.Button(panel, label='Enter', pos=(20, 130))# Init
        self.my_btn.Bind(wx.EVT_BUTTON, self.calc_all) # Method

        self.Show() # Runs the Show method, defined in line 5

    def get_box_value(self, event): # Pass the current instance (the name) and the event (what happened)
        print(self.first_box.GetValue()) # Runs whatever is found inside of the first box
        print(self.second_box.GetValue()) # Runs whatever is found inside of the second box
    
    def calc_all(self, event):
        """
        cost for all materials ( THAT ARE CONSTANTS )
        """
        price_concrete = 150 
        price_joist = 24.07
        price_studs = 2.72



        """
        Part one- Chemai
        """
        """
        length = int(input("What's length of your house?: "))
        width = int(input("What's width of your house?: "))
        height = 8
        """
        length = int(self.first_box.GetValue())
        width =  int(self.second_box.GetValue())
        height = 8

        # convertion to inchs 
        length = (length*12)
        width = (width*12)
        height = (height*12)


        # perimeter
        perimeter = (2 * length) + (2 * width)

        # walls of the basement
        Volume1 = (length) * (width) * (height)# needs to be 400
        Volume2 = (length + 16) * (width + 16) * (height)
        Volume = (Volume2-Volume1)

        # floor of the basement
        floor_Volume = ((length*width)*4)

        # footers of the basement
        footer_Volume1= (length + 24) + (width + 24)
        footer_Volume2= (length - 24) + (width - 24)
        footer_Volume = ((footer_Volume1 - footer_Volume2)*8)

        # convertion to feet
        perimeter = perimeter/12
        Volume = Volume/1728
        footer_Volume = footer_Volume/8
        floor_Volume = floor_Volume/1728

        # convertion to yards
        Volume = Volume/27
        footer_Volume = footer_Volume/27
        floor_Volume = floor_Volume/27
        Volume = round(Volume, 2)
        footer_Volume = round(footer_Volume, 2)
        floor_Volume = round(floor_Volume, 2)

        # Total concrete calculation
        Total_cost_concrete = ((Volume + footer_Volume)* 150) 
        Total_cost_concrete = round(Total_cost_concrete, 2)
        """
        Part two- Sasha
        """


        length_joist = 16
        width_joist = 2 
        heigt_joist = 10

        length_of_house = length
        distance = (length_of_house - 1.5)
        number_of_joists = distance / 16
        number_of_joists = round(number_of_joists)

        joistrow = (width) / (16)
        joistrow = round(joistrow)
        total_joist = (joistrow) * (number_of_joists)

        cost_joist = number_of_joists * 24.07
        cost_joist = round (cost_joist, 2)


        """
        Part two- Keegang
        """
        length_internal = (length / 12) - 0.75 #These 2 lines subtract half of the length of one stud from both the length and the width. This is so they're not just sticking half out of the wall.
        width_internal = (width / 12) - 0.75

        perimeter_feet = (length_internal * 2) + (width_internal * 2) #Get perimeter in linear feet
        perimeter_in_inches = perimeter_feet * 12 #Convert perimeter to completely in inches

        studs = 0; # Defining studs variable
        while perimeter_in_inches > 16:   #Calculates number of studs
            perimeter_in_inches = perimeter_in_inches - 16
            studs = studs + 1
        studs = studs + 4 #Adding 1 stud for every corner. This is, of course, assuming it's just a square.

        cost_studs = studs * 2.72 #Calculates cost
        cost_studs = round(cost_studs, 2)
        cost_of_everything = cost_joist + cost_studs + Total_cost_concrete

        #PRINTS PRINTS PRINTS
        #CHEMAI PRINTS 
        def state():
            return """
            The perimeter of your house is: """ + str(perimeter) + """
            The Volume of the wall is: """ + str(Volume) + (" Cubic yard.")+"""
            The Volume of the footer is:""" + str(footer_Volume) + (" Cubic yard.")+"""\n
            The Volume of a concrete floor for your basement is:""" + str(floor_Volume) + (" Cubic yards.")+"""\n
            
            Total Cost of concrete: """ + str(Total_cost_concrete)+ "$" +"""\n
            
            The total number of joists needed is """ + str(number_of_joists)+"""\n
            Total cost of joists: """ + str(cost_joist) + "$"+"""\n
          
            Number of studs: """ + str(studs)+ """\n

            Total cost of studs: $""" + str(cost_studs)+"""\n

            
            Total cost : """ + str(cost_of_everything) + "$!"
            

        self.report.SetValue(state())


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()















