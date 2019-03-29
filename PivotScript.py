from com.snaplogic.scripting.language import ScriptHook
from com.snaplogic.scripting.language.ScriptHook import *
  
class TransformScript(ScriptHook):
    def __init__(self, input, output, error, log):
        self.input = input
        self.output = output
        self.error = error
        self.log = log
  
    def execute(self):
        self.log.info("Executing Transform script")
        i = 1
        while self.input.hasNext():
            data = self.input.next()
            dataoutkey = data['Key']
            for x in range(1, 13):
                dataout = {}
                monthkey = 'Month' + str(x).zfill(2)
                dataout['key'] = dataoutkey
                dataout['monthkey'] = monthkey
                dataout['value'] = data[monthkey]
                self.output.write(dataout)
                x = x + 1
        self.log.info("Finished executing the Transform script")
 
hook = TransformScript(input, output, error, log)