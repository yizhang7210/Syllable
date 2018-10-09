package com.syllable.exchange.events;

import com.syllable.exchange.models.ExchangeEvent;

public interface EventBus {

    void publish(ExchangeEvent event);
}
