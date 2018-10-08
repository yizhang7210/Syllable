package com.syllable.exchange.events;

public interface EventBus {

    void publish(ExchangeEvent event);
}
