 import subprocess                                                               
                                                                                   
  def djtest():                                                                   
      cmd =['python', 'manager/manage.py', 'runserver']                                                                 
      subprocess.run(cmd)    