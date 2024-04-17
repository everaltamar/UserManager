from userManager import api
from userManager.controllers import user_manager_controller
from userManager.controllers import auth_login_controller


api.add_resource(user_manager_controller.CreateUser ,"/api/v1/users/createUser")
api.add_resource(user_manager_controller.UpdateUser ,"/api/v1/users/updateUser")
api.add_resource(user_manager_controller.GetUsers ,"/api/v1/users/getUsers")
api.add_resource(user_manager_controller.GetUser ,"/api/v1/users/getUser")
api.add_resource(user_manager_controller.DeleteUser ,"/api/v1/users/deleteUser")
api.add_resource(auth_login_controller.LoginUser ,"/api/v1/users/login")







