package com.syllable.exchange.models;

import org.springframework.data.annotation.Id;

public class SyllableUser {

    @Id
    private String id;
    private String username;
    private String password;

    public String getId() {
        return id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
