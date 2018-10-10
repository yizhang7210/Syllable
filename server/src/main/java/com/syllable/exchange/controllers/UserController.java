package com.syllable.exchange.controllers;

import com.syllable.exchange.daos.SyllableUserDao;
import com.syllable.exchange.models.SyllableUser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;



@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private SyllableUserDao userDao;

    @PostMapping("/sign-up")
    public void signUp(@RequestBody SyllableUser syllableUser) {
        syllableUser.setPassword(new BCryptPasswordEncoder().encode(syllableUser.getPassword()));
        userDao.save(syllableUser);
    }
}
