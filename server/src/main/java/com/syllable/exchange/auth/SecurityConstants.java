package com.syllable.exchange.auth;

public class SecurityConstants {
    //TODO: Read this from Environment Variable through application.properties
    static final String SECRET = "SyllableForTheWin";
    static final long EXPIRATION_TIME = 864_000_000; // 10 days
    static final String TOKEN_PREFIX = "Bearer ";
    static final String HEADER_STRING = "Authorization";
    public static final String SIGN_UP_URL = "/users/sign-up";
}