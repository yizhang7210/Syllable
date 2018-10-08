package com.syllable.exchange.commands;

import com.syllable.exchange.dtos.PredictionDto;
import com.syllable.exchange.events.EventBus;
import com.syllable.exchange.events.EventDao;
import com.syllable.exchange.events.PredictionCreated;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class PredictionCommand {

    @Autowired
    private EventDao eventDao;

    @Autowired
    private EventBus eventBus;

    public void createPrediction(PredictionDto predictionBody) {
        PredictionCreated event = new PredictionCreated(predictionBody);
        eventDao.save(event);
        eventBus.publish(event);
    }
}
