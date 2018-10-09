package com.syllable.exchange.events;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.syllable.exchange.dtos.PredictionDto;

import java.time.LocalDateTime;

public class PredictionCreated extends ExchangeEvent {

    private static final String EVENT_NAME = "PredictionCreated";

    public PredictionCreated(PredictionDto prediction) {
        try {
            this.name = EVENT_NAME;
            this.payload = jsonMapper.writeValueAsString(prediction);
            this.target = EventTarget.PREDICTION;
            this.createdAt = LocalDateTime.now();
        } catch (JsonProcessingException e) {
            throw new RuntimeException("Prediction cannot be serialized.");
        }
    }
}
