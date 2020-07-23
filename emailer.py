import smtplib
import sys
from datetime import datetime
def banner():
      user_selection
      print('''
                                 __                           
 _______  __ _____    ___/ /__   ___ ________ ________ 
/ __/ _ \/ // / _ \  / _  / -_) / _ `/ __/ _ `/ __/ -_)
\__/\___/\_,_/ .__/  \_,_/\__/  \_, /_/  \_,_/\__/\__/ 
            /_/                /___/                ''' )
      print("                                     by: alienBLue")
      print("[****************************************************************]")
      print("[****************************************************************]")
      while user_selection != "Y" or user_selection != "N":
            user_selection = input("                        Do you wish to continue: Y/N")
            user_selection.upper()
            if user_selection == "N":
                  exit(0)
      


class emailer:
  senate1_email = None
  senate1_name = None
  senate2_email = None
  senate2_name = None 
  message = " Testing "
  email = " "
  trump1 = "contact@victory.donaldtrump.com"
  counter = 0
  
  def __init__(self):
        print("[****************************************************************]")
        print("[****************************************************************]")
        # chose which state your from
        self.email = raw_input("Which State are you from? ex. NY, NJ, FL. Then press Enter key: ")
        self.email = self.email.upper()
        print("[****************************************************************]")
        print("[****************************************************************]")
       

  def the_senate(self):

    if (self.email == 'AK'):
          self.senate1_email = "Senator_Stevens@stevens.senate.gov"
          self.senate1_name = "Senator Stevens"
          self.senate2_email = "email@murkowski.senate.gov"
          self.senate2_name = "Senator Murkowski"
    elif( self.email == 'AL'):
          self.senate1_email = "senator@shelby.senate.gov"
          self.senate1_name = "Senator Shelby"
    elif (self.email == 'AR'):
          self.senate1_email = "senator@bumpers.senate.gov"
          self.senate1_name = "Senator Bumpers"
          self.senate2_email = "senator.hutchinson@hutchinson.senate.gov"
          self.senate2_name = "Senator Hutchinson"
    elif (self.email == 'AZ'):
          self.senate1_email = "info@kyl.senate.gov"
          self.senate1_name = "Senator Kyl"
          self.senate2_email = "Senator_McCain@mccain.senate.gov"
          self.senate2_name = "Senator McCain"
    elif (self.email == 'CA'):
          self.senate1_email = "senator@boxer.senate.gov"
          self.senate1_name = "Senator Boxer"
          self.senate2_email = "senator@feinstein.senate.gov"
          self.senate2_name = "Senator Feinstein"
    elif (self.email == 'CO'):
          self.senate1_email = "data@nighthorse.falcontech.com"
          self.senate1_name = "Senator Campbell"
    elif (self.email == 'CT'):
          self.senate1_email = "sen_dodd@dodd.senate.gov"
          self.senate1_name = "Senator Dodd"
          self.senate2_email = "senator_lieberman@lieberman.senate.gov"
          self.senate2_name = "Senator Lieberman"
    elif (self.email == 'DE'):
          self.senate1_email = "senator@biden.senate.gov"
          self.senate1_name = "Senator Biden"
    elif (self.email == 'FL'):
          self.senate1_email = "bob_graham@graham.senate.gov"
          self.senate1_name = "Senator Graham"
          self.senate2_email = "connie@mack.senate.gov"
          self.senate2_name = "Senator Mack"
    elif (self.email == 'GA'):
          self.senate1_email = "senator_max_cleland@cleland.senate.gov"
          self.senate1_name = "Senator Cleland"
          self.senate2_email = "senator_coverdell@coverdell.senate.gov"
          self.senate2_name = "Senator Coverdell" 
    elif (self.email == 'HI'):
          self.senate1_email = "senator@inouye.senate.gov"
          self.senate1_name = "Senator Inouye"
    elif (self.email == 'IA'):
          self.senate1_email = "tom_harkin@harkin.senate.gov"
          self.senate1_name = "Senator Harkin"
          self.senate2_email = "chuck_grassley@grassley.senate.gov"
          self.senate2_name = "Senator Grassley"   
    elif (self.email == 'ID'):
          self.senate1_email = "larry_craig@craig.senate.gov"
          self.senate1_name = "Senator Craig"
          self.senate2_email = "dirk_kempthorne@kempthorne.senate.gov"
          self.senate2_name = "Senator Kempthorne" 
    elif (self.email == 'IL'):
          self.senate1_email = "senator@moseley-braun.senate.gov"
          self.senate1_name = "Senator Moseley-Braun"
    elif (self.email == 'IN'):
          self.senate1_email = "lugar@iquest.net"
          self.senate1_name = "Senator Lugar"
    elif (self.email == 'KS'):
          self.senate1_email = "sam_brownback@brownback.senate.gov"
          self.senate1_name = "Senator Brownback"
    elif (self.email == 'KY'):
          self.senate1_email = "wendell_ford@ford.senate.gov"
          self.senate1_name = "Senator Ford"
          self.senate2_email = "senator@mcconnell.senate.gov"
          self.senate2_name = "Senator McConnell" 
    elif (self.email == 'LA'):
          self.senate1_email = "senator@breaux.senate.gov"
          self.senate1_name = "Senator Breaux"
          self.senate2_email = "senator@landrieu.senate.gov"
          self.senate2_name = "Senator Landrieu"
    elif (self.email == 'MA'):
          self.senate1_email = "john_kerry@kerry.senate.gov"
          self.senate1_name = "Senator Kerry"
          self.senate2_email = "senator@kennedy.senate.gov"
          self.senate2_name = "Senator Kennedy" 
    elif (self.email == 'MD'):
          self.senate1_email = "senator@mikulski.senate.gov"
          self.senate1_name = "Senator Mikulski"
          self.senate2_email = "senator@sarbanes.senate.gov"
          self.senate2_name = "Senator Sarbanes"  
    elif (self.email == 'ME'):
          self.senate1_email = "olympia@snowe.senate.gov"
          self.senate1_name = "Senator Snowe"
          self.senate2_email = "senator@collins.senate.gov"
          self.senate2_name = "Senator Collins"
    elif (self.email == 'MI'):
          self.senate1_email = "senator@levin.senate.gov"
          self.senate1_name = "Senator Levin"
          self.senate2_email = "michigan@abraham.senate.gov"
          self.senate2_name = "Senator Abraham"  
    elif (self.email == 'MN'):
          self.senate1_email = "senator@wellstone.senate.gov"
          self.senate1_name = "Senator Wellstone"
          self.senate2_email = "mail_grams@grams.senate.gov"
          self.senate2_name = "Senator Grams"
    elif (self.email == 'MO'):
          self.senate1_email = "kit_bond@bond.senate.gov"
          self.senate1_name = "Senator Bond"
          self.senate2_email = "john_ashcroft@ashcroft.senate.gov"
          self.senate2_name = "Senator Ashcroft" 
    elif (self.email == 'MS'):
          self.senate1_email = "senatorlott@lott.senate.gov"
          self.senate1_name = "Senator Lott"
          self.senate2_email = "senator@cochran.senate.gov"
          self.senate2_name = "Senator Cochran"
    elif (self.email == 'MT'):
          self.senate1_email = "max@baucus.senate.gov"
          self.senate1_name = "Senator Baucus"
          self.senate2_email = "conrad_burns@burns.senate.gov"
          self.senate2_name = "Senator Burns" 
    elif (self.email == 'NC'):
          self.senate1_email = "senator@faircloth.senate.gov"
          self.senate1_name = "Senator Faircloth"
          self.senate2_email = "jesse_helms@helms.senate.gov"
          self.senate2_name = "Senator Helms" 
    elif (self.email == 'ND'):
          self.senate1_email = "senator@conrad.senate.gov"
          self.senate1_name = "Senator Conrad"
          self.senate2_email = "senator@dorgan.senate.gov"
          self.senate2_name = "Senator Dorgan"
    elif (self.email == 'NE'):
          self.senate1_email = "chuck_hagel@hagel.senate.gov"
          self.senate1_name = "Senator Hagel"
          self.senate2_email = "bob@kerrey.senate.gov"
          self.senate2_name = "Senator Kerrey"
    elif (self.email == 'NH'):
          self.senate1_email = "mailbox@gregg.senate.gov"
          self.senate1_name = "Senator Gregg"
          self.senate2_email = "opinion@smith.senate.gov"
          self.senate2_name = "Senator Smith" 
    elif (self.email == 'NJ'):
          self.senate1_email = "senator_torricelli@torricelli.senate.gov"
          self.senate1_name = "Senator Torricelli"
          self.senate2_email = "frank_lautenberg@lautenberg.senate.gov"
          self.senate2_name = "Senator Lautenberg"
    elif (self.email == 'NM'):
          self.senate1_email = "Senator_Bingaman@bingaman.senate.gov"
          self.senate1_name = "Senator Bingaman"
          self.senate2_email = "senator_domenici@domenici.senate.gov"
          self.senate2_name = "Senator Domenici"
    elif (self.email == 'NV'):
          self.senate1_email = "senator_reid@reid.senate.gov"
          self.senate1_name = "Senator Reid"
          self.senate2_email = "senator@bryan.sen.gov"
          self.senate2_name = "Senator Bryan" 
    elif (self.email == 'NY'):
          self.senate1_email = "Senator@dpm.senate.gov"
          self.senate1_name = "Senator Moynihan"
          self.senate2_email = "senator_al@damato.senate.gov"
          self.senate2_name = "Senator D'Amato"  
    elif (self.email == 'OH'):
          self.senate1_email = "Senator_Glenn@glenn.senate.gov"
          self.senate1_name = "Senator Glenn"
          self.senate2_email = "senator_dewine@dewine.senate.gov"
          self.senate2_name = "Senator Dewine"    
    elif (self.email == 'OK'):
          self.senate1_email = "nickles@rpc.senate.gov"
          self.senate1_name = "Senator Nickles"
    elif (self.email == 'OR'):
          self.senate1_email = "wyden@teleport.com"
          self.senate1_name = "Senator Wyden"
    elif (self.email == 'PA'):
          self.senate1_email = "senator@santorum.senate.gov"
          self.senate1_name = "Senator Santorum"
          self.senate2_email = "senator_specter@specter.senate.gov"
          self.senate2_name = "Senator Specter"
    elif (self.email == 'RI'):
          self.senate1_email = "senator_chafee@chafee.senate.gov"
          self.senate1_name = "Senator Chafee"   
    elif (self.email == 'SC'):
          self.senate1_email = "senator@hollings.senate.gov"
          self.senate1_name = "Senator Hollings"
          self.senate2_email = "senator@thurmond.senate.gov"
          self.senate2_name = "Senator Thurmond" 
    elif (self.email == 'SD'):
          self.senate1_email = "tom_daschle@daschle.senate.gov"
          self.senate1_name = "Senator Daschle"
          self.senate2_email = "tim_johnson@johnson.senate.gov"
          self.senate2_name = "Senator Johnson"
    elif (self.email == 'TN'):
          self.senate1_email = "senator_thompson@thompson.senate.gov"
          self.senate1_name = "Senator Thompson"
          self.senate2_email = "senator_frist@frist.senate.gov"
          self.senate2_name = "Senator Frist"
    elif (self.email == 'TX'):
          self.senate1_email = "senator@hutchison.senate.gov"
          self.senate1_name = "Senator Hutchison"
          self.senate2_email = "info@gramm96.org"
          self.senate2_name = "Senator Gramm"
    elif (self.email == 'UH'):
          self.senate1_email = "senator_hatch@hatch.senate.gov"
          self.senate1_name = "Senator Hatch"
          self.senate2_email = "senator@bennett.senate.gov"
          self.senate2_name = "Senator Bennett"
    elif (self.email == 'VA'):
          self.senate1_email = "senator@robb.senate.gov"
          self.senate1_name = "Senator Robb"
          self.senate2_email = "senator@warner.senate.gov"
          self.senate2_name = "Senator Warner"
    elif (self.email == 'VT'):
          self.senate1_email = "senator_leahy@leahy.senate.gov"
          self.senate1_name = "Senator Leahy"
          self.senate2_email = "vermont@jeffords.senate.gov"
          self.senate2_name = "Senator Jeffords"
    elif (self.email == 'WA'):
          self.senate1_email = "senator_murray@murray.senate.gov"
          self.senate1_name = "Senator Murray"
          self.senate2_email = "Senator_Gorton@gorton.senate.gov"
          self.senate2_name = "Senator Gorton"
    elif (self.email == 'WI'):
          self.senate1_email = "senator@feingold.senate.gov"
          self.senate1_name = "Senator Feingold"
          self.senate2_email = "senator_kohl@kohl.senate.gov"
          self.senate2_name = "Senator Kohl"
    elif (self.email == 'WV'):
          self.senate1_email = "Senator_Byrd@Byrd.Senate.gov"
          self.senate1_name = "Senator Byrd"
          self.senate2_email = "senator@rockefeller.senate.gov"
          self.senate2_name = "Senator Rockerfeller"
    elif (self.email == 'WY'):
          self.senate1_email = "craig@thomas.senate.gov"
          self.senate1_name = "Senator Thomas"
          self.senate2_email = "senator@enzi.senate.gov"
          self.senate2_name = "Senator Enzi"
    else:
          print("Restart Program and Enter Valid State in proper Format")
          exit(1)
     # choose your mode
  def mode(self):
    
    self.mode = int(input("How many Emails would you like to send? \n 1 || 50 emails || 2 || 100 emails || 3 || 150 emails: \n"))
    print("[****************************************************************]")
    print("[****************************************************************]")
    mode = self.mode 
    if self.mode > 4:
        print("          Restart Program and Enter Valid mode")
        exit(1)
    else:
         print("            You've selected Mode number: {}" .format(self.mode))
         print("[****************************************************************]")
         print("[****************************************************************]")
  # establishing connection to email server
  def setup_server(self):
      self.email_provider = 0
      while self.email_provider == 0 or self.email_provider > 4:
        self.email_provider = int(input("Choose your Email Provider : \n 1 || Gmail  2 || Yahoo 3 || Outlook  4 || HotMail: \n Then Press Enter: "))
      self.username = raw_input("Enter Username: \n")
      self.pwd = raw_input("Enter Password: \n")
      if self.email_provider == 1:
        self.s = smtplib.SMTP("smtp.gmail.com", 587)
      elif self.email_provider == 2:
        self.s = smtplib.SMTP("smtp.mail.yahoo.com", 465)
      elif self.email_provider == 3:
        self.s = smtplib.SMTP("	smtp.live.com", 587)
      elif self.email_provider == 4:
        self.s = smtplib.SMTP("	smtp.live.com", 465)
      self.s.ehlo()
      self.s.starttls()
      self.s.ehlo()
      self.s.login(self.username, self.pwd)
      print("[****************************************************************]")
      print("[****************************************************************]")
      print("                 SERVER CONNECTION ESTABLISHED")
      print("[****************************************************************]")
      print("[****************************************************************]")
  
  #loop 
  def mailing(self):
      if self.mode == 1:
        self.amount = 50
      elif self.mode == 2:
        self.amount = 100
      elif self.mode == 3:
        self.amount = 150
      elif self.mode == 4:
            self.amount = int(input("Enter amount: \n"))
      subj = "ATTEN:"
      date = (datetime.date(datetime.now()))
      msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( self.username, self.senate1_email, subj, date, self.message)
      for i in range(self.amount):
          self.s.sendmail(self.username, self.senate1_email, msg)
          #self.s.sendmail( self.username, self.trump1, self.message)
          #if self.senate2_email != None:
           # self.s.sendmail( self.username, self.senate2_email, self.message)
          self.counter += 3
          print("[****************************************************************]")
          print("[****************************************************************]")
          print("                       {} Payloads Sent".format(self.counter))
      print("[****************************************************************]")
      print("[****************************************************************]")
      print("                         Transmission Completed") 
      self.s.close()
      print("[****************************************************************]")
      print("[****************************************************************]")
      print("                        CONNECTION TERMINATED")


if __name__ == "__main__":
    banner()
    trump = emailer()
    trump.the_senate()
    trump.setup_server()
    trump.mode()
    trump.mailing()
    print(trump.email)
    print(trump.senate1_email) 
    print(trump.senate1_name)
    print(trump.mode)
         