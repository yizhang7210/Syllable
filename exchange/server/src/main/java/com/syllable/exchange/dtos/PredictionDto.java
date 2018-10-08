package com.syllable.exchange.dtos;


import org.springframework.data.annotation.Id;

import java.util.Date;


public class PredictionDto {
    @Id
    private String id;

    private String title;

    private Date expiry;

    public PredictionDto(String title, Date expiry) {
        this.title = title;
        this.expiry = expiry;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Date getExpiry() {
        return expiry;
    }

    public void setExpiry(Date expiry) {
        this.expiry = expiry;
    }

    @Override
    public String toString() {
        return String.format(
                "PredictionDto[id=%s, title=%s, expiry=%s]",
                id, title, expiry);
    }
}
