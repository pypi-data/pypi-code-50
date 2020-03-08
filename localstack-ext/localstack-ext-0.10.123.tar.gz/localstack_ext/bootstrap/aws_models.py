from localstack.utils.aws import aws_models
OwQyT=super
OwQyn=None
OwQyS=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  OwQyT(LambdaLayer,self).__init__(arn)
  self.cwd=OwQyn
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,OwQyS,env=OwQyn):
  OwQyT(RDSDatabase,self).__init__(OwQyS,env=env)
 def name(self):
  return self.OwQyS.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
