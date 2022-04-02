from enum import Enum
from importlib.metadata import distributions

from scipy import stats
import numpy as np
import math as math

class Distribution_Type( Enum ):
    continuos = 1
    discrete  = 2

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_ 



class Distribution:
    def __init__( self, name, default_args, dist, description, dist_type = Distribution_Type.continuos ) -> None:
        if not isinstance( dist_type, Distribution_Type ):
            raise ValueError( "dist_type must be Distribution_Type.continuos or Distribution_Type.discrete" )

        self.name = name
        self.default_args = default_args
        self.type = dist_type
        self.dist = dist
        self.description = description
        self.params = list( filter( lambda key: key != "loc" and key != "scale", default_args.keys() ) )



# Distributions to check, shape constants were taken from the examples on the scipy.stats distribution documentation pages.
DISTRIBUTIONS = [
    Distribution( name = "alpha",           default_args = { "a": 3.57, "loc": 0.0, "scale": 1.0 },                                  dist = stats.alpha,           description = "" ), 
    Distribution( name = "anglit",          default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.anglit,          description = "" ), 
    Distribution( name = "arcsine",         default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.arcsine,         description = "" ), 
    Distribution( name = "beta",            default_args = { "a": 2.31, "b": 0.627, "loc": 0.0, "scale": 1.0 },                      dist = stats.beta,            description = "" ), 
    Distribution( name = "betaprime",       default_args = { "a": 5, "b": 6, "loc": 0.0, "scale": 1.0 },                             dist = stats.betaprime,       description = "" ), 
    Distribution( name = "bradford",        default_args = { "c": 0.299, "loc": 0.0, "scale": 1.0 },                                 dist = stats.bradford,        description = "" ), 
    Distribution( name = "burr",            default_args = { "c": 10.5, "d": 4.3, "loc": 0.0, "scale": 1.0 },                        dist = stats.burr,            description = "" ), 
    Distribution( name = "cauchy",          default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.cauchy,          description = "" ), 
    Distribution( name = "chi",             default_args = { "df": 78, "loc": 0.0, "scale": 1.0 },                                   dist = stats.chi,             description = "" ), 
    Distribution( name = "chi2",            default_args = { "df": 55, "loc": 0.0, "scale": 1.0 },                                   dist = stats.chi2,            description = "" ), 
    Distribution( name = "cosine",          default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.cosine,          description = "" ), 
    Distribution( name = "dgamma",          default_args = { "a": 1.1, "loc": 0.0, "scale": 1.0 },                                   dist = stats.dgamma,          description = "" ), 
    Distribution( name = "dweibull",        default_args = { "c": 2.07, "loc": 0.0, "scale": 1.0 },                                  dist = stats.dweibull,        description = "" ), 
    Distribution( name = "erlang",          default_args = { "a": 2, "loc": 0.0, "scale": 1.0 },                                     dist = stats.erlang,          description = "" ), 
    Distribution( name = "expon",           default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.expon,           description = "" ), 
    Distribution( name = "expon",           default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.expon,           description = "" ), 
    Distribution( name = "exponnorm",       default_args = { "K": 1.5, "loc": 0.0, "scale": 1.0 },                                   dist = stats.exponnorm,       description = "" ), 
    Distribution( name = "exponweib",       default_args = { "a": 2.89, "c": 1.95, "loc": 0.0, "scale": 1.0 },                       dist = stats.exponweib,       description = "" ), 
    Distribution( name = "exponpow",        default_args = { "b": 2.7, "loc": 0.0, "scale": 1.0 },                                   dist = stats.exponpow,        description = "" ), 
    Distribution( name = "f",               default_args = { "dfn": 29, "dfd": 18, "loc": 0.0, "scale": 1.0 },                       dist = stats.f,               description = "" ), 
    Distribution( name = "fatiguelife",     default_args = { "c": 29, "loc": 0.0, "scale": 1.0 },                                    dist = stats.fatiguelife,     description = "" ), 
    Distribution( name = "fisk",            default_args = { "c": 3.09, "loc": 0.0, "scale": 1.0 },                                  dist = stats.fisk,            description = "" ), 
    Distribution( name = "foldcauchy",      default_args = { "c": 4.72, "loc": 0.0, "scale": 1.0 },                                  dist = stats.foldcauchy,      description = "" ), 
    Distribution( name = "foldnorm",        default_args = { "c": 1.95, "loc": 0.0, "scale": 1.0 },                                  dist = stats.foldnorm,        description = "" ), 
    Distribution( name = "genlogistic",     default_args = { "c": 0.412, "loc": 0.0, "scale": 1.0 },                                 dist = stats.genlogistic,     description = "" ), 
    Distribution( name = "genpareto",       default_args = { "c": 0.1, "loc": 0.0, "scale": 1.0 },                                   dist = stats.genpareto,       description = "" ), 
    Distribution( name = "genpareto",       default_args = { "c": 0.1, "loc": 0.0, "scale": 1.0 },                                   dist = stats.genpareto,       description = "" ), 
    Distribution( name = "gennorm",         default_args = { "beta": 1.3, "loc": 0.0, "scale": 1.0 },                                dist = stats.gennorm,         description = "" ), 
    Distribution( name = "genexpon",        default_args = { "a": 9.13, "b": 16.2, "c": 3.28, "loc": 0.0, "scale": 1.0 },            dist = stats.genexpon,        description = "" ), 
    Distribution( name = "genextreme",      default_args = { "c": -0.1, "loc": 0.0, "scale": 1.0 },                                  dist = stats.genextreme,      description = "" ), 
    Distribution( name = "gausshyper",      default_args = { "a": 13.8, "b": 3.12, "c": 2.51, "z": 5.18, "loc": 0.0, "scale": 1.0 }, dist = stats.gausshyper,      description = "" ), 
    Distribution( name = "gamma",           default_args = { "a": 1.99, "loc": 0.0, "scale": 1.0 },                                  dist = stats.gamma,           description = "" ), 
    Distribution( name = "gengamma",        default_args = { "a": 4.42, "c": -3.12, "loc": 0.0, "scale": 1.0 },                      dist = stats.gamma,           description = "" ), 
    Distribution( name = "genhalflogistic", default_args = { "c": 0.773, "loc": 0.0, "scale": 1.0 },                                 dist = stats.genhalflogistic, description = "" ), 
    Distribution( name = "gilbrat",         default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.gilbrat,         description = "" ), 
    Distribution( name = "gompertz",        default_args = { "c": 0.947, "loc": 0.0, "scale": 1.0 },                                 dist = stats.gompertz,        description = "" ), 
    Distribution( name = "gumbel_r",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.gumbel_r,        description = "" ), 
    Distribution( name = "gumbel_l",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.gumbel_l,        description = "" ), 
    Distribution( name = "halfcauchy",      default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.halfcauchy,      description = "" ), 
    Distribution( name = "halflogistic",    default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.halflogistic,    description = "" ), 
    Distribution( name = "halfnorm",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.halfnorm,        description = "" ), 
    Distribution( name = "halfgennorm",     default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.halfgennorm,     description = "" ), 
    Distribution( name = "hypsecant",       default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.hypsecant,       description = "" ), 
    Distribution( name = "invgamma",        default_args = { "a": 4.07, "loc": 0.0, "scale": 1.0 },                                  dist = stats.invgamma,        description = "" ), 
    Distribution( name = "invgauss",        default_args = { "mu": 0.145, "loc": 0.0, "scale": 1.0 },                                dist = stats.invgauss,        description = "" ), 
    Distribution( name = "invweibull",      default_args = { "c": 10.6, "loc": 0.0, "scale": 1.0 },                                  dist = stats.invweibull,      description = "" ), 
    Distribution( name = "johnsonsb",       default_args = { "a": 4.32, "b": 3.18, "loc": 0.0, "scale": 1.0 },                       dist = stats.johnsonsb,       description = "" ), 
    Distribution( name = "johnsonsu",       default_args = { "a": 2.25, "b": 2.25, "loc": 0.0, "scale": 1.0 },                       dist = stats.johnsonsu,       description = "" ), 
    Distribution( name = "ksone",           default_args = { "n": 1e+03, "loc": 0.0, "scale": 1.0 },                                 dist = stats.ksone,           description = "" ), 
    Distribution( name = "kstwobign",       default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.kstwobign,       description = "" ), 
    Distribution( name = "laplace",         default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.laplace,         description = "" ), 
    Distribution( name = "levy",            default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.levy,            description = "" ), 
    Distribution( name = "levy_l",          default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.levy_l,          description = "" ), 
    Distribution( name = "levy_stable",     default_args = { "alpha": 0.357, "beta": -0.675, "loc": 0.0, "scale": 1.0 },             dist = stats.levy_stable,     description = "" ), 
    Distribution( name = "logistic",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.logistic,        description = "" ), 
    Distribution( name = "loggamma",        default_args = { "c": 0.414, "loc": 0.0, "scale": 1.0 },                                 dist = stats.loggamma,        description = "" ), 
    Distribution( name = "loglaplace",      default_args = { "c": 3.25, "loc": 0.0, "scale": 1.0 },                                  dist = stats.loglaplace,      description = "" ), 
    Distribution( name = "lognorm",         default_args = { "s": 0.954, "loc": 0.0, "scale": 1.0 },                                 dist = stats.lognorm,         description = "" ), 
    Distribution( name = "lomax",           default_args = { "c": 1.88, "loc": 0.0, "scale": 1.0 },                                  dist = stats.lomax,           description = "" ), 
    Distribution( name = "maxwell",         default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.maxwell,         description = "" ), 
    Distribution( name = "mielke",          default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.mielke,          description = "" ), 
    Distribution( name = "nakagami",        default_args = { "nu": 4.97, "loc": 0.0, "scale": 1.0 },                                 dist = stats.nakagami,        description = "" ), 
    Distribution( name = "ncx2",            default_args = { "df": 21, "nc": 1.06, "loc": 0.0, "scale": 1.0 },                       dist = stats.ncx2,            description = "" ), 
    Distribution( name = "ncf",             default_args = { "dfn": 27, "dfd": 27, "nc": 0.416, "loc": 0.0, "scale": 1.0 },          dist = stats.ncf,             description = "" ), 
    Distribution( name = "nct",             default_args = { "df": 14, "nc": 0.24, "loc": 0.0, "scale": 1.0 },                       dist = stats.nct,             description = "" ), 
    Distribution( name = "norm",            default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.norm,            description = "" ), 
    Distribution( name = "pareto",          default_args = { "b": 2.62, "loc": 0.0, "scale": 1.0 },                                  dist = stats.pareto,          description = "" ), 
    Distribution( name = "pearson3",        default_args = { "skew": 0.1, "loc": 0.0, "scale": 1.0 },                                dist = stats.pearson3,        description = "" ), 
    Distribution( name = "powerlaw",        default_args = { "a": 1.66, "loc": 0.0, "scale": 1.0 },                                  dist = stats.powerlaw,        description = "" ), 
    Distribution( name = "powerlognorm",    default_args = { "c": 2.14, "s": 0.446, "loc": 0.0, "scale": 1.0 },                      dist = stats.powerlognorm,    description = "" ), 
    Distribution( name = "powernorm",       default_args = { "c": 4.45, "loc": 0.0, "scale": 1.0 },                                  dist = stats.powernorm,       description = "" ), 
    Distribution( name = "rdist",           default_args = { "c": 0.9, "loc": 0.0, "scale": 1.0 },                                   dist = stats.rdist,           description = "" ), 
    Distribution( name = "reciprocal",      default_args = { "a": 0.00623, "b": 1.01, "loc": 0.0, "scale": 1.0 },                    dist = stats.reciprocal,      description = "" ), 
    Distribution( name = "rayleigh",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.rayleigh,        description = "" ), 
    Distribution( name = "rice",            default_args = { "b": 0.775, "loc": 0.0, "scale": 1.0 },                                 dist = stats.rice,            description = "" ), 
    Distribution( name = "recipinvgauss",   default_args = { "mu": 0.63, "loc": 0.0, "scale": 1.0 },                                 dist = stats.recipinvgauss,   description = "" ), 
    Distribution( name = "semicircular",    default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.semicircular,    description = "" ), 
    Distribution( name = "t",               default_args = { "df": 2.74, "loc": 0.0, "scale": 1.0 },                                 dist = stats.t,               description = "" ), 
    Distribution( name = "triang",          default_args = { "c": 0.158, "loc": 0.0, "scale": 1.0 },                                 dist = stats.triang,          description = "" ), 
    Distribution( name = "truncexpon",      default_args = { "b": 4.69, "loc": 0.0, "scale": 1.0 },                                  dist = stats.truncexpon,      description = "" ), 
    Distribution( name = "truncnorm",       default_args = { "a": 0.1, "b": 2, "loc": 0.0, "scale": 1.0 },                           dist = stats.truncnorm,       description = "" ), 
    Distribution( name = "tukeylambda",     default_args = { "lam": 3.13, "b": 2, "loc": 0.0, "scale": 1.0 },                        dist = stats.tukeylambda,     description = "" ), 
    Distribution( name = "tukeylambda",     default_args = { "lam": 3.13, "loc": 0.0, "scale": 1.0 },                                dist = stats.tukeylambda,     description = "" ), 
    Distribution( name = "uniform",         default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.uniform,         description = "" ), 
    Distribution( name = "vonmises",        default_args = { "kappa":3.99, "loc": 0.0, "scale": 1.0 },                               dist = stats.vonmises,        description = "" ), 
    Distribution( name = "vonmises_line",   default_args = { "kappa":3.99, "loc": 0.0, "scale": 1.0 },                               dist = stats.vonmises_line,   description = "" ), 
    Distribution( name = "wald",            default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.wald,            description = "" ), 
    Distribution( name = "weibull_min",     default_args = { "c":1.79, "loc": 0.0, "scale": 1.0 },                                   dist = stats.weibull_min,     description = "" ), 
    Distribution( name = "weibull_max",     default_args = { "c":2.87, "loc": 0.0, "scale": 1.0 },                                   dist = stats.weibull_max,     description = "" ), 
    Distribution( name = "wrapcauchy",      default_args = { "c":0.0311, "loc": 0.0, "scale": 1.0 },                                 dist = stats.wrapcauchy,      description = "" )
]


print( DISTRIBUTIONS[0].params )