from localstack.utils.aws import aws_models
OEfqU=super
OEfqx=None
OEfqC=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  OEfqU(LambdaLayer,self).__init__(arn)
  self.cwd=OEfqx
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,OEfqC,env=OEfqx):
  OEfqU(RDSDatabase,self).__init__(OEfqC,env=env)
 def name(self):
  return self.OEfqC.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
