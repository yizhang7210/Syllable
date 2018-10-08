package com.syllable.exchange.services;

import com.syllable.exchange.dtos.PredictionDto;
import org.springframework.stereotype.Service;

@Service
public class PredictionService {
    public PredictionDto createPrediction(PredictionDto predictionBody) {
        return predictionBody;
    }
}
