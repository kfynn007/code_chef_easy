package com.ampene.calc1.calculator;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;




public interface UserRepository extends  JpaRepository<User, Long> {
    User findByEmail(String email);
}
