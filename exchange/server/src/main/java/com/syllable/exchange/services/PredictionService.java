package com.syllable.exchange.services;

import com.syllable.exchange.commands.PredictionCommand;
import com.syllable.exchange.dtos.PredictionDto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PredictionService {

    @Autowired
    private PredictionCommand predictionCommand;

    public PredictionDto createPrediction(PredictionDto predictionBody) {
        predictionCommand.createPrediction(predictionBody);
        return predictionBody;
    }
}
