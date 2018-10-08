package com.syllable.exchange.events;

import org.springframework.data.annotation.Id;

public abstract class ExchangeEvent {

    @Id
    public String id;

    public String name;

    public String payLoad;

    public EventTarget target;

}
