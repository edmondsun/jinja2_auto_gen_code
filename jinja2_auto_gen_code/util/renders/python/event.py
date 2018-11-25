

class LoginFail(BaseEvt):
	"""Class docs
	"""
    

	   def __init__(self,remote,user):
        """init docs
        """
        super(LoginFail,self).__init__()
            self.remote = remote
            self.user = user
            self.msg = "User [{user}] from [{remote}] failed to log in.".format(remote=self.remote,user=self.user)
    





class LoginSuccess(BaseEvt):
	"""Class docs
	"""
    

	   def __init__(self,remote,user):
        """init docs
        """
        super(LoginSuccess,self).__init__()
            self.remote = remote
            self.user = user
            self.msg = "User [{user}] logged in from [{remote}].".format(remote=self.remote,user=self.user)
    





class LogoutSuccess(BaseEvt):
	"""Class docs
	"""
    

	   def __init__(self,remote,user):
        """init docs
        """
        super(LogoutSuccess,self).__init__()
            self.remote = remote
            self.user = user
            self.msg = "User [{user}] logged out from [{remote}].".format(remote=self.remote,user=self.user)
    



