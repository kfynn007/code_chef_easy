package com.ampene.calc1.calculator;




public interface UserService {

    public User findUserByEmail(String email);
    public void saveUser(User user);


}
