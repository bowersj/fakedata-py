from datetime import datetime
from enum import Enum

from scipy import stats
import numpy as np
import math as math

class distribution_Type( Enum ):
    continuos = 1
    discrete  = 2

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_ 



class distribution:
    def __init__( self, name, default_args, dist, dist_type = distribution_Type.continuos ) -> None:
        if not isinstance( dist_type, distribution_Type ):
            raise ValueError( "dist_type must be distribution_Type.continuos or distribution_Type.discrete" )

        self.batch_size = 1000
        self.name = name
        self.default_args = default_args
        self.type = dist_type
        self.dist = dist
        self.params = list( filter( lambda key: key != "loc" and key != "scale", default_args.keys() ) )
        self.index = -1
        self.default_args[ "size" ] = self.batch_size
        self._random_numbers = dist.rvs( **self.default_args )

    def _update_distribution( self, **kargs ) -> None:
        for k in self.params:
            if k not in kargs:
                raise ValueError( f"{k} is not a supported parameter." )
        
        self.default_args = kargs

    def _generate_random_numbers( self ) -> None:
        self.default_args[ "size" ] = self.batch_size
        self._random_numbers = self.dist.rvs( **self.default_args )
        self.index = -1

    def random_number( self ):
        if self.index < self.batch_size:
            self.index += 1
            return self._random_numbers[ self.index ]
        else:
            self._generate_random_numbers()
            return self.random_number()



#distributions to check, shape constants were taken from the examples on the scipy.stats distribution documentation pages.
start = datetime.now()
DISTRIBUTIONTS = [

        distribution(
            name = "alpha",
            default_args = { "a": 3.57, "loc": 0.0, "scale": 1.0 },
            dist = stats.alpha

        ), 

        distribution(
            name = "anglit",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.anglit

        ),  

        distribution(
            name = "arcsine",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.arcsine

        ), 

        distribution(
            name = "beta",
            default_args = { "a": 2.31, "b": 0.627, "loc": 0.0, "scale": 1.0 },
            dist = stats.beta

        ), 

        distribution(
            name = "betaprime",
            default_args = { "a": 5, "b": 6, "loc": 0.0, "scale": 1.0 },
            dist = stats.betaprime

        ), 

        distribution(
            name = "bradford",
            default_args = { "c": 0.299, "loc": 0.0, "scale": 1.0 },
            dist = stats.bradford

        ), 

        distribution(
            name = "burr",
            default_args = { "c": 10.5, "d": 4.3, "loc": 0.0, "scale": 1.0 },
            dist = stats.burr

        ), 

        distribution(
            name = "cauchy",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.cauchy

        ), 

        distribution(
            name = "chi",
            default_args = { "df": 78, "loc": 0.0, "scale": 1.0 },
            dist = stats.chi

        ), 

        distribution(
            name = "chi2",
            default_args = { "df": 55, "loc": 0.0, "scale": 1.0 },
            dist = stats.chi2

        ), 

        distribution(
            name = "cosine",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.cosine

        ), 

        distribution(
            name = "dgamma",
            default_args = { "a": 1.1, "loc": 0.0, "scale": 1.0 },
            dist = stats.dgamma

        ), 

        distribution(
            name = "dweibull",
            default_args = { "c": 2.07, "loc": 0.0, "scale": 1.0 },
            dist = stats.dweibull

        ), 

        distribution(
            name = "erlang",
            default_args = { "a": 2, "loc": 0.0, "scale": 1.0 },
            dist = stats.erlang

        ), 

        distribution(
            name = "expon",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.expon

        ), 

        distribution(
            name = "exponnorm",
            default_args = { "K": 1.5, "loc": 0.0, "scale": 1.0 },
            dist = stats.exponnorm

        ), 

        distribution(
            name = "exponweib",
            default_args = { "a": 2.89, "c": 1.95, "loc": 0.0, "scale": 1.0 },
            dist = stats.exponweib

        ), 

        distribution(
            name = "exponpow",
            default_args = { "b": 2.7, "loc": 0.0, "scale": 1.0 },
            dist = stats.exponpow,

        ), 

        distribution(
            name = "f",
            default_args = { "dfn": 29, "dfd": 18, "loc": 0.0, "scale": 1.0 },
            dist = stats.f

        ), 

        distribution(
            name = "fatiguelife",
            default_args = { "c": 29, "loc": 0.0, "scale": 1.0 },
            dist = stats.fatiguelife

        ), 

        distribution(
            name = "fisk",
            default_args = { "c": 3.09, "loc": 0.0, "scale": 1.0 },
            dist = stats.fisk

        ), 

        distribution(
            name = "foldcauchy",
            default_args = { "c": 4.72, "loc": 0.0, "scale": 1.0 },
            dist = stats.foldcauchy

        ), 

        distribution(
            name = "foldnorm",
            default_args = { "c": 1.95, "loc": 0.0, "scale": 1.0 },
            dist = stats.foldnorm

        ), 

        distribution(
            name = "genlogistic",
            default_args = { "c": 0.412, "loc": 0.0, "scale": 1.0 },
            dist = stats.genlogistic

        ), 

        distribution(
            name = "genpareto",
            default_args = { "c": 0.1, "loc": 0.0, "scale": 1.0 },
            dist = stats.genpareto

        ), 

        distribution(
            name = "gennorm",
            default_args = { "beta": 1.3, "loc": 0.0, "scale": 1.0 },
            dist = stats.gennorm

        ), 

        distribution(
            name = "genexpon",
            default_args = { "a": 9.13, "b": 16.2, "c": 3.28, "loc": 0.0, "scale": 1.0 },
            dist = stats.genexpon

        ), 

        distribution(
            name = "genextreme",
            default_args = { "c": -0.1, "loc": 0.0, "scale": 1.0 },
            dist = stats.genextreme

        ), 

        distribution(
            name = "gausshyper",
            default_args = { "a": 13.8, "b": 3.12, "c": 2.51, "z": 5.18, "loc": 0.0, "scale": 1.0 },
            dist = stats.gausshyper

        ), 

        distribution(
            name = "gamma",
            default_args = { "a": 1.99, "loc": 0.0, "scale": 1.0 },
            dist = stats.gamma

        ), 

        distribution(
            name = "gengamma",
            default_args = { "a": 4.42, "loc": 0.0, "scale": 1.0 },
            dist = stats.gamma

        ), 

        distribution(
            name = "genhalflogistic",
            default_args = { "c": 0.773, "loc": 0.0, "scale": 1.0 },
            dist = stats.genhalflogistic

        ), 

        distribution(
            name = "gilbrat",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.gilbrat

        ), 

        distribution(
            name = "gompertz",
            default_args = { "c": 0.947, "loc": 0.0, "scale": 1.0 },
            dist = stats.gompertz

        ), 

        distribution(
            name = "gumbel_r",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.gumbel_r

        ), 

        distribution(
            name = "gumbel_l",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.gumbel_l

        ), 

        distribution(
            name = "halfcauchy",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.halfcauchy

        ), 

        distribution(
            name = "halflogistic",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.halflogistic

        ), 

        distribution(
            name = "halfnorm",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.halfnorm
        ), 

        distribution(
            name = "halfgennorm",
            default_args = { "loc": 0.0, "scale": 1.0, "beta": 1.0 },
            dist = stats.halfgennorm

        ), 

        distribution(
            name = "hypsecant",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.hypsecant

        ), 

        distribution(
            name = "invgamma",
            default_args = { "a": 4.07, "loc": 0.0, "scale": 1.0 },
            dist = stats.invgamma

        ), 

        distribution(
            name = "invgauss",
            default_args = { "mu": 0.145, "loc": 0.0, "scale": 1.0 },
            dist = stats.invgauss

        ), 

        distribution(
            name = "invweibull",
            default_args = { "c": 10.6, "loc": 0.0, "scale": 1.0 },
            dist = stats.invweibull

        ), 

        distribution(
            name = "johnsonsb",
            default_args = { "a": 4.32, "b": 3.18, "loc": 0.0, "scale": 1.0 },
            dist = stats.johnsonsb

        ), 

        distribution(
            name = "johnsonsu",
            default_args = { "a": 2.25, "b": 2.25, "loc": 0.0, "scale": 1.0 },
            dist = stats.johnsonsu

        ), 

        distribution(
            name = "ksone",
            default_args = { "n": 1e+03, "loc": 0.0, "scale": 1.0 },
            dist = stats.ksone

        ), 

        distribution(
            name = "kstwobign",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.kstwobign

        ), 

        distribution(
            name = "laplace",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.laplace

        ), 

        distribution(
            name = "levy",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.levy

        ), 

        distribution(
            name = "levy_l",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.levy_l

        ), 

        distribution(
            name = "levy_stable",
            default_args = { "alpha": 0.357, "beta": -0.675, "loc": 0.0, "scale": 1.0 },
            dist = stats.levy_stable

        ), 

        distribution(
            name = "logistic",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.logistic

        ), 

        distribution(
            name = "loggamma",
            default_args = { "c": 0.414, "loc": 0.0, "scale": 1.0 },
            dist = stats.loggamma

        ), 

        distribution(
            name = "loglaplace",
            default_args = { "c": 3.25, "loc": 0.0, "scale": 1.0 },
            dist = stats.loglaplace

        ), 

        distribution(
            name = "lognorm",
            default_args = { "s": 0.954, "loc": 0.0, "scale": 1.0 },
            dist = stats.lognorm

        ), 

        distribution(
            name = "lomax",
            default_args = { "c": 1.88, "loc": 0.0, "scale": 1.0 },
            dist = stats.lomax

        ), 

        distribution(
            name = "maxwell",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.maxwell

        ), 

        distribution(
            name = "mielke",
            default_args = { "loc": 0.0, "scale": 1.0, "k": 1.0, "s": 1.0 },
            dist = stats.mielke

        ), 

        distribution(
            name = "nakagami",
            default_args = { "nu": 4.97, "loc": 0.0, "scale": 1.0 },
            dist = stats.nakagami

        ), 

        distribution(
            name = "ncx2",
            default_args = { "df": 21, "nc": 1.06, "loc": 0.0, "scale": 1.0 },
            dist = stats.ncx2

        ), 

        distribution(
            name = "ncf",
            default_args = { "dfn": 27, "dfd": 27, "nc": 0.416, "loc": 0.0, "scale": 1.0 },
            dist = stats.ncf

        ), 

        distribution(
            name = "nct",
            default_args = { "df": 14, "nc": 0.24, "loc": 0.0, "scale": 1.0 },
            dist = stats.nct

        ), 

        distribution(
            name = "norm",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.norm

        ), 

        distribution(
            name = "pareto",
            default_args = { "b": 2.62, "loc": 0.0, "scale": 1.0 },
            dist = stats.pareto

        ), 

        distribution(
            name = "pearson3",
            default_args = { "skew": 0.1, "loc": 0.0, "scale": 1.0 },
            dist = stats.pearson3

        ), 

        distribution(
            name = "powerlaw",
            default_args = { "a": 1.66, "loc": 0.0, "scale": 1.0 },
            dist = stats.powerlaw

        ), 

        distribution(
            name = "powerlognorm",
            default_args = { "c": 2.14, "s": 0.446, "loc": 0.0, "scale": 1.0 },
            dist = stats.powerlognorm

        ), 

        distribution(
            name = "powernorm",
            default_args = { "c": 4.45, "loc": 0.0, "scale": 1.0 },
            dist = stats.powernorm

        ), 

        distribution(
            name = "r",
            default_args = { "c": 0.9, "loc": 0.0, "scale": 1.0 },
            dist = stats.rdist

        ), 

        distribution(
            name = "reciprocal",
            default_args = { "a": 0.00623, "b": 1.01, "loc": 0.0, "scale": 1.0 },
            dist = stats.reciprocal

        ), 

        distribution(
            name = "rayleigh",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.rayleigh

        ), 

        distribution(
            name = "rice",
            default_args = { "b": 0.775, "loc": 0.0, "scale": 1.0 },
            dist = stats.rice

        ), 

        distribution(
            name = "recipinvgauss",
            default_args = { "mu": 0.63, "loc": 0.0, "scale": 1.0 },
            dist = stats.recipinvgauss

        ), 

        distribution(
            name = "semicircular",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.semicircular

        ), 

        distribution(
            name = "t",
            default_args = { "df": 2.74, "loc": 0.0, "scale": 1.0 },
            dist = stats.t

        ), 

        distribution(
            name = "triang",
            default_args = { "c": 0.158, "loc": 0.0, "scale": 1.0 },
            dist = stats.triang

        ), 

        distribution(
            name = "truncexpon",
            default_args = { "b": 4.69, "loc": 0.0, "scale": 1.0 },
            dist = stats.truncexpon

        ), 

        distribution(
            name = "truncnorm",
            default_args = { "a": 0.1, "b": 2, "loc": 0.0, "scale": 1.0 },
            dist = stats.truncnorm

        ), 

        distribution(
            name = "tukeylambda",
            default_args = { "lam": 3.13, "loc": 0.0, "scale": 1.0 },
            dist = stats.tukeylambda

        ), 

        distribution(
            name = "tukeylambda",
            default_args = { "lam": 3.13, "loc": 0.0, "scale": 1.0 },
            dist = stats.tukeylambda

        ), 

        distribution(
            name = "uniform",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.uniform

        ), 

        distribution(
            name = "vonmises",
            default_args = { "kappa":3.99, "loc": 0.0, "scale": 1.0 },
            dist = stats.vonmises

        ), 

        distribution(
            name = "vonmises_line",
            default_args = { "kappa":3.99, "loc": 0.0, "scale": 1.0 },
            dist = stats.vonmises_line

        ), 

        distribution(
            name = "wald",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.wald

        ), 

        distribution(
            name = "weibull_min",
            default_args = { "c":1.79, "loc": 0.0, "scale": 1.0 },
            dist = stats.weibull_min

        ), 

        distribution(
            name = "weibull_max",
            default_args = { "c":2.87, "loc": 0.0, "scale": 1.0 },
            dist = stats.weibull_max

        ), 

        distribution(
            name = "wrapcauchy",
            default_args = { "c":0.0311, "loc": 0.0, "scale": 1.0 },
            dist = stats.wrapcauchy
        )

]
end = datetime.now()
diff = end - start
secs = diff.total_seconds()
print( DISTRIBUTIONTS[0].params )
print( f"seconds: {secs}" )
print( f"Distribution: {len( DISTRIBUTIONTS )}" )
print( f"Distribution per Second: {len( DISTRIBUTIONTS ) / secs }" )