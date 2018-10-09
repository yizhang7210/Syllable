package com.syllable.exchange.events;

import com.syllable.exchange.models.ExchangeEvent;
import org.springframework.stereotype.Component;

@Component
public class EventBusImpl implements EventBus{

    @Override
    public void publish(ExchangeEvent event) {

    }
}
